#!/bin/bash
clear
echo "------------------------------------------"
echo "   🎮 Z4XGAMING MASTER CONTROLLER 🎮"
echo "------------------------------------------"

# 1. Sabhi changes ko add karo
git add .

# 2. Commit message pooncho
echo "📝 Website mein kya badla? (Enter description):"
read msg

if [ -z "$msg" ]; then
    msg="Auto Update from Termux"
fi

git commit -m "$msg"

# 3. GitHub par push karo (Token pehle se saved hai)
echo "🚀 Lovable AI aur GitHub ko update kar raha hoon..."
git push origin main

echo "------------------------------------------"
echo "✅ SUCCESS: Website Level-Up Ho Gayi!"
echo "🤖 Lovable AI changes dekh raha hai..."
echo "------------------------------------------"
