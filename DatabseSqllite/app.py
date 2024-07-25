import sqlite3

conn=sqlite3.connect('youtube_videos.db')

cursor=conn.cursor()

cursor.execute(''' 
    CREATE Table if not exists videos(
                id INTEGER PRIMARY KEY,
                name text not null,
                time text not null
    )
''')

def list_videos():

    cursor.execute('SELECT * from videos ')
    if cursor.rowcount==-1:
        print("Empty Db.... ")
    for row in cursor.fetchall():
        print(row)

def add_video(name ,time):
    cursor.execute("Insert into videos (name ,time) values (?,?)",(name,time))
    conn.commit()

def update_video(videoid ,newname ,newtime):
    cursor.execute("Update videos set name=? ,time=? where id=?",(newname ,newtime, videoid))
    conn.commit()

def delete_video(videoid):
    conn.execute("delete from videos where id=?",(videoid,))
    conn.commit()

def main():
    while True:
        print("\n Youtube Manager with Db ")
        print('1. List all the youtube videos ')
        print('2. Add a youtube video ')
        print('3. Update a youtube video ')
        print('4. delete a youtube video ')
        print('5. Exit a app ')
        choice=input("Enter your choice: ")
        # print(videos)
        if choice=='1':
            list_videos()
        elif choice=='2':
            name=input("Enter the video name: ")
            time=input("Enter the video time: ")
            add_video(name,time)
        elif choice=='3':
            videoid=input('Enter video id to update: ')
            name=input("Enter the video name: ")
            time=input("Enter the video time: ")
            update_video(videoid,name,time)
        elif choice=='4':
            videoid=input('Enter video id to delete: ')
            delete_video(videoid)
        elif choice=='5':
            break
        else:
            print('Invalid choice ')
    
    conn.close()


if __name__=='__main__':
    main()