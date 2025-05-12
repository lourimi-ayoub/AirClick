import cv2
import numpy as np
import mediapipe as mp
import autopy
import time

# Initialize MediaPipe Hands
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

# Camera setup
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# Get screen size for mouse movement
screen_width, screen_height = autopy.screen.size()
pTime = 0  # For FPS calculation
frame_reduction = 100  # Reduce frame area to prevent edge detection issues
smoothening = 5  # Smoothing factor
plocX, plocY = 0, 0  # Previous locations
clocX, clocY = 0, 0  # Current locations

while True:
    success, img = cap.read()
    if not success:
        break
        
    # Flip image for mirror effect
    img = cv2.flip(img, 1)
    
    # Convert to RGB for MediaPipe
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))

            if lmList:
                # Index Finger Tip (Landmark 8)
                x1, y1 = lmList[8][1:]  
                # Middle Finger Tip (Landmark 12)
                x2, y2 = lmList[12][1:]  

                # Check which fingers are up
                fingers = []
                # Thumb
                if lmList[4][1] > lmList[3][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                # Other fingers
                for id in [8, 12, 16, 20]:
                    if lmList[id][2] < lmList[id-2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                # Only move mouse if index finger is up and middle finger is down
                if fingers[1] == 1 and fingers[2] == 0:
                    # Convert coordinates
                    x3 = np.interp(x1, (frame_reduction, wCam-frame_reduction), (0, screen_width))
                    y3 = np.interp(y1, (frame_reduction, hCam-frame_reduction), (0, screen_height))
                    
                    # Smoothen values
                    clocX = plocX + (x3 - plocX) / smoothening
                    clocY = plocY + (y3 - plocY) / smoothening
                    
                    # Ensure coordinates are within screen bounds
                    clocX = max(0, min(clocX, screen_width-1))
                    clocY = max(0, min(clocY, screen_height-1))
                    
                    # Move mouse
                    autopy.mouse.move(clocX, clocY)
                    plocX, plocY = clocX, clocY

                # Click gesture - when both index and middle fingers are up
                if fingers[1] == 1 and fingers[2] == 1:
                    distance = np.hypot(x2 - x1, y2 - y1)
                    if distance < 30:  # Threshold for click
                        autopy.mouse.click()

            # Draw hand landmarks on the image
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # Calculate and display FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the image
    cv2.imshow("Virtual Mouse", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()