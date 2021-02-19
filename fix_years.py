import os 
import re
  
def main(): 
	for count, filename in enumerate(os.listdir()): #run through all folder/files
		if not os.path.isdir(filename):
			continue # Not a directory
		match = re.findall(r"\d+",filename) #find all whole numbers in the folder's name. Put in in a list called match
		match = [i for i in match if 1920 <= int(i) <= 2021] # delete all identified numbers which are not between 1920 and 2021
		if match:
			# Then it found a match!
			year=str(match[-1]) #take the last value in the list. This will skip all the other years in the title of the album. For example in < Artist - The best of 1998 [1988] FLAC >
			if filename.find("-")+1==filename.find(year): 
				continue # skip if the directory is already named something like <Author> -<year>- <Album>. Should be done manually
			if filename.find("-")+2==filename.find(year):
				continue # skip if the directory is already named something like <Author> - <year> - <Album>. Already what I want. 
			new_filename=rreplace(filename,year,"",1) #delete the last occurence of year in the foldername
			new_filename=new_filename.replace(" - "," - "+year+" - ",1)
			os.rename(filename, new_filename) #comment this if only testing
			print(filename+"   ----->    "+new_filename+"    DONE")

def rreplace(s, old, new, count):
	return (s[::-1].replace(old[::-1], new[::-1], count))[::-1] # reverses all the strings in question, performs an ordinary replacement using str.replace on the reversed strings, then reverses the result back the right way round

if __name__ == '__main__': 
    # Calling main() function 
    main() 
