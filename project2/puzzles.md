# Puzzle 1

Plaintext: I got a jar of dirt

Operations:
1. Vigenère — Decode — key: `dirt`
2. Substitute (QWERTY keyboard → standard alphabet) — Decode
   - Plaintext field: `QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm`
   - Ciphertext field: `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`
3. Base64 — Decode (From Base64, alphabet `A-Za-z0-9+/=`)
4. Binary — Decode (From Binary, delimiter Space, byte length 8)

# Puzzle 2 

Plaintext: NOT ALL TREASURES SILVER AND GOLD MATE

Operations:
1. Mono-alphabetic Substitution — Decode — key from hint 1: digits 0–9 map to `CYBERISFUN`, so C→0, Y→1, B→2, E→3, R→4, I→5, S→6, F→7, U→8, N→9 
2. Columnar Transposition — Decode — 5 columns, key `ABCDE` (no reordering), "Keep spaces" enabled, mode: write by rows, read by columns
3. Multi-tap Phone (SMS) Cipher — Decode — repeated digits map to keypad letters, `0` = space
4. Atbash — Decode 