import cv2
import mediapipe as mp
import pyautogui
import time

# -----------------------------
# Game keys
# -----------------------------
BRAKE_KEY = 'left'
ACC_KEY   = 'right'

time.sleep(2)

current_key_pressed = set()

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

# Fingertip landmark ids
tipIds = [4, 8, 12, 16, 20]

# Camera (use MSMF for your system)
video = cv2.VideoCapture(0, cv2.CAP_MSMF)

with mp_hand.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:

    while True:

        keyPressed = False
        key_count = 0
        key_pressed = None

        ret, image = video.read()
        if not ret:
            print("Camera not working")
            break

        image = cv2.flip(image, 1)

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        rgb.flags.writeable = False
        results = hands.process(rgb)
        rgb.flags.writeable = True

        lmList = []

        if results.multi_hand_landmarks:
            myHand = results.multi_hand_landmarks[0]

            h, w, c = image.shape

            for id, lm in enumerate(myHand.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

            mp_draw.draw_landmarks(
                image,
                myHand,
                mp_hand.HAND_CONNECTIONS
            )

        fingers = []

        if len(lmList) != 0:

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Other 4 fingers
            for i in range(1, 5):
                if lmList[tipIds[i]][2] < lmList[tipIds[i] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            total = fingers.count(1)

            # ---------------- BRAKE ----------------
            if total == 0:

                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "BRAKE", (45, 375),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)

                pyautogui.keyDown(BRAKE_KEY)
                current_key_pressed.add(BRAKE_KEY)

                key_pressed = BRAKE_KEY
                keyPressed = True
                key_count += 1

            # ------------- ACCELERATE --------------
            elif total == 5:

                cv2.rectangle(image, (20, 300), (470, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "ACCELERATE", (45, 375),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)

                pyautogui.keyDown(ACC_KEY)
                current_key_pressed.add(ACC_KEY)

                key_pressed = ACC_KEY
                keyPressed = True
                key_count += 1

        # ------------- Key release logic -------------
        if not keyPressed and len(current_key_pressed) != 0:
            for key in current_key_pressed:
                pyautogui.keyUp(key)
            current_key_pressed = set()

        elif key_count == 1 and len(current_key_pressed) == 2:
            for key in current_key_pressed:
                if key != key_pressed:
                    pyautogui.keyUp(key)
            current_key_pressed = {key_pressed}

        cv2.imshow("Gesture Control", image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Clean exit
for key in current_key_pressed:
    pyautogui.keyUp(key)

video.release()
cv2.destroyAllWindows()