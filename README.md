# Reddit Comments Sentiment Analysis 

## Authors: Alex Wernex and Zachery Linscott

This is a program to download the HTML pages of multiple URLs pointing to Reddit posts.

## How it works:

1. Each URL is read from a file that the user of the program provides a path to.
2. The raw HTML of each URL is then put into separate files.
3. From there the HTML is "scrubbed" to extract the comments from the subreddit.  
4. The cleaned comments are stored in files unique to each post.
5. The comments files are scanned and sentiment analysis is performed on each comment.  
6. Once the sentiments are gathered, they are also put into their own files, unique for each Reddit post.
7. Each sentiment file is then put into its own bar graph.
   - The user can visually see the num of pos., neg., and neutral comments.  
8. These graphs appear and are stored in a folder as well.

## How to Use

1. Ensure you are in the correct directory.

2. Make sure to download the environment from requirements.yaml to make sure you have the appropriate libraries.
   - If you don't, no biggie, the program will just take a little longer, to install the dependencies during runtime.

4. Run in the terminal using python passing the file of urls you wish to gather comments from as an argument, e.g.: `python run.py yourfilepath/yourfilename`
   
5. Finally when you are finished viewing the graphs, exit out of all of the windows to end the program.
Don't worry, all of the graphs will still be in the plots folder as pictures. 

Also, make sure you ran the run.py with the old.reddit link for each one. Otherwise the comments will not be in the file and it won't work.

## Sample Output

The attached Data/raw/HTMLOutput files, Data/processed/comments files, Data/sentiments/sentiments, and Data/Plots/graphs files 
are all sample outputs.
