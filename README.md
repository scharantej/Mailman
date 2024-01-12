 ## **Flask Application Design for Email Service**

### **HTML Files**

**1. index.html**
- This is the main HTML file that will serve as the user interface for the email service.
- It should include a form with fields for the sender's email address, recipient's email address, subject, and message body.
- It should also have a submit button that triggers the sending of the email.

**2. success.html**
- This HTML file will be displayed after the email has been successfully sent.
- It should include a message confirming that the email was sent successfully.

**3. error.html**
- This HTML file will be displayed if there is an error sending the email.
- It should include a message explaining the error and instructions on how to resolve it.

### **Routes**

**1. /send_email**
- This route will handle the submission of the email form.
- It will extract the data from the form and use it to send an email using Flask's built-in `send_mail()` function.
- If the email is sent successfully, it will redirect to the `success.html` page.
- If there is an error sending the email, it will redirect to the `error.html` page.

**2. /success**
- This route will simply display the `success.html` page.

**3. /error**
- This route will simply display the `error.html` page.

### **Additional Notes**

- The Flask application will need to be configured to use a mail server.
- This can be done by setting the `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USERNAME`, and `MAIL_PASSWORD` environment variables.
- For more information on configuring Flask to send emails, refer to the Flask documentation.