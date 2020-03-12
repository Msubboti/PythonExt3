Countries = "France, Ukraine, America, Egypt, Poland"
Hello = "Welcome to California!"
Listing =Countries.split(', ')
print(Listing)

for contry in Listing:
    print(Hello[0:11] + contry + Hello[-1])