<h1>Zoom Attendance Tracker</h1>
<h4>
This Flask app automates Zoom meeting attendance by 
  receiving Zoom webhook events and updating a Google Sheet in real-time. It logs participant email, status (present/left), join and leave timestamps, and meeting topics. The app uses the Google Sheets API with service account credentials to access and update the spreadsheet. For local development and testing, ngrok exposes the Flask server to receive live Zoom events. Simply configure the Zoom webhook to point to the ngrok URL, and the app handles attendance updates automatically. Easy to set up and customize for any Zoom-based attendance tracking.</h4>
