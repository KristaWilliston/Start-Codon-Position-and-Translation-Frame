# Start-Codon-Position-and-Translation-Frame
The program finds the position and the translation frame of the start codon 'ATG'

I used the .find function to find the position that ATG appears on in the string.  I then used this position and divided it by 3 since a codon is made up of 3 nucleotides.  I added 1 to this because I am adding back the fact that strings start with a position of 0 and not 1 so I will get the translation frame output to read correctly with the position of the codon in the translation frame.  I had a lot of trouble with this problem.  I didn't understand at first why the % 3 + 1 section would work I was reading it more as a division then addition problem instead of reading it as partitioning the position every 3 positions then adding 1 for the frame translation.
