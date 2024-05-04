#Face Perceptron
printf "\n%s\n" "Face Perceptron" >> face_perceptron_results.txt
for c in {1..10}; do
  printf "%s%s\n" $c "0%" >> face_perceptron_results.txt
  for i in {1..5}; do
    python classification/ReadData.py $"-f" $"-p" $c
  done
done


##Digit Perceptron
#printf "\n%s\n" "Digit Perceptron" >> results.txt
#for c in {1..10}; do
#  printf "%s%s\n" $c "0%" >> results.txt
#  for i in {1..5}; do
#    python ReadData.py $"-d" $"-p" $c
#  done
#done

