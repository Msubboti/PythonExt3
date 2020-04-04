import psycopg2
import cgi, cgitb



form = cgi.FieldStorage()
name_of_film = form.getvalue('name_of_film')

dictionary = {'Forrest_Gump': "Forrest Gump", 'Inception': "Inception",
              'Leon': "Leon", 'Schindler_List': "Schindler List",
              'The_Green_Mile': "The Green Mile", 'The_Shawshank_Redemption': "The Shawshank Redemption",
              'The_Dark_Knight': "The Dark Knight", 'The_Fifth_Element': "The Fifth Element",
              'Catch_Me_If_You_Can': "Catch Me If You Can", 'Saving_Private_Ryan': "Saving Private Ryan"}
file = open(r'D:/Python/Database/cgi-bin/htm_page.txt', "r")
print("Content-type: text/html")
print()
for line in file:
    if "{}" in line:
        print(line.format(dictionary[name_of_film]))
    else:
        print(line)
print("<h1>Welcome to short summary of '{}' film.</h1>".format(dictionary[name_of_film]))
print('<div id="answer_film">')
print(' <p><img src="../big_film_img/{}.jpeg" width="450" height="600"></p>'.format(name_of_film))
print('</div>')
print('<div class= "Description">')
conn = psycopg2.connect(dbname='films', user='postgres', password='bombardier')
cursor = conn.cursor()
cursor.execute("SELECT id, name_of_film FROM film_name where name_of_film='{}'".format(dictionary[name_of_film]))
row = cursor.fetchone()
print("""    
<div class = "Strings">
    <p>Film is: </p>
    <p>Director is: </p>
    <p>Year: </p>
    <p>Starring: </p>
</div>""")
cursor.execute("SELECT d.name, d.surname, year FROM films f inner "
               "join directors d on (f.director = d.id) where name_of_film={} ".format(row[0]))
information = cursor.fetchone()

cursor.execute("SELECT a.name, a.surname_first FROM casting c inner "
               "join actors a on (c.id_film = a.id) where id_film={} ".format(row[0]))
actors = cursor.fetchone()

cursor.execute("SELECT * FROM casting where id_film={} ".format(row[0]))
actors = cursor.fetchone()

number_of_actors = len(actors)

staring = []
for item in range(1, 7):

    cursor.execute("SELECT name, surname_first, surname_second  FROM actors where id={} ".format(actors[item]))
    name_actors = cursor.fetchone()
    string = ""
    for name in name_actors:
        if name == 'N/A':
            pass
        else:
            string += ' ' + name
    staring.append(string[1:])
    string = ""


print("""
<div class = "text">
<p>{0}</p>
<p>{1} {2}</p>
<p>{3}</p>""".format(row[1], information[0], information[1], information[2]))
for item in staring:
    print("<p>{}</p>".format(item))
staring = []
print("</div>")
