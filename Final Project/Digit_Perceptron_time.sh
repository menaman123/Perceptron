#Digit Perceptron
printf "\n%s\n" "Digit Perceptron" >> Digit_Perceptron_time-to-train.txt
for c in {1..10}; do
  printf "%s%s\n" $c "0%" >> Digit_Perceptron_time-to-train.txt
  for i in {1..5}; do
    python classification/ReadData.py $"-d" $"-p" $c
  done
done
