import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib



def send_email():
        from main import speak
        from main import take_user_input
        try:
            speak("Sure sir. I need recipient's email address.")
            speak("How would you like to provide recipient's email address?")
            choice_in_recipient = take_user_input()

            if "voice" in choice_in_recipient.lower() or "say" in choice_in_recipient.lower() or "tell" in choice_in_recipient.lower() or "speak" in choice_in_recipient.lower():
                print("Recipient address: ")
                recipient_email = take_user_input()
                recipient_email = recipient_email.strip().lower()
                recipient_email = recipient_email.replace(" ", "")
                print("Recipient address: ", recipient_email)
            elif "type" in choice_in_recipient.lower() or "write" in choice_in_recipient.lower():
                recipient_email = input("Recipient's Email Address: ")
                print("Recipient address: ", recipient_email)
            else:
                speak("Invalid way, you can provide me email address by  typing or by saying it.")
                return

            speak("I need subject of your email.")
            speak("How would you like to provide subject?")
            choice_in_subject = take_user_input()
            if "voice" in choice_in_subject.lower() or "say" in choice_in_subject.lower() or "tell" in choice_in_subject.lower() or "speak" in choice_in_recipient.lower():
                subject =  take_user_input()
                print("Subject: ", subject)
                if "exit" in subject.lower():
                    return 
            elif "type" in choice_in_subject.lower() or "write" in choice_in_subject.lower():
                subject = input("Write your subject: ")
                print("Subject: ", subject)
                if "exit" in subject.lower():
                    return 
            else:
                speak("Unable to create subject of your email sir.")
                return

            speak("How will you provide me the message sir?")
            choice_in_message = take_user_input()
            if "voice" in choice_in_message.lower() or "say" in choice_in_message.lower() or "tell" in choice_in_message.lower() or "speak" in choice_in_recipient.lower():
                message =  take_user_input()
                print("Message: ", message)
                if "exit" in message.lower():
                    return 
            elif "type" in choice_in_message.lower() or "write" in choice_in_message.lower():
                message = input("Write your message: ")
                print("Message: ", message)
                if "exit" in message.lower():
                    return 
            else:
                speak("Unable to create message of your email sir.")
                return

            # Your email credentials and SMTP server details
            sender_email = "sigdelprabin321@gmail.com"
            ohoo = "omet osmk kavu tlrw"
            smtp_server = "smtp.gmail.com"
            smtp_port = 587  # or 465 for SSL

            # Create MIMEMultipart message
            message_content = MIMEMultipart()
            message_content['From'] = sender_email
            message_content['To'] = recipient_email
            message_content['Subject'] = subject

            # Attach message content
            message_content.attach(MIMEText(message, 'plain'))

            # Attachment functionality
            speak("Do you have anything to attach here sir ?")
            attach_choice = take_user_input()

            if 'yes' in attach_choice.lower() or 'yeah' in attach_choice.lower() or 'offcourse' in attach_choice.lower() or 'of course' in attach_choice.lower():
                print("Please provide the file path sir")
                file_path = input("Enter your file path:\n")

                if os.path.exists(file_path):
                    # Open the file in binary mode
                    with open(file_path, 'rb') as attachment:
                        # Add file as application/octet-stream
                        # Email client can usually download this automatically as attachment
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())

                    # Encode file in ASCII characters to send via email
                    encoders.encode_base64(part)
                    # Add header as key/value pair to attachment part
                    part.add_header(
                        'Content-Disposition',
                        f'attachment; filename= {os.path.basename(file_path)}'
                    )
                    # Add attachment to message and convert message to string
                    message_content.attach(part)
                else:
                    print("File not found. Attachment skipped.")

            # Create SMTP server connection
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Secure the connection
            server.login(sender_email, ohoo)  # Login to your email account

            # Construct the email message
            email_message = message_content.as_string()

            speak("Please confirm the email content. Subject: {}. Message: {}. Do you want to proceed? (Yes or No)".format(subject, message))
            confirm = take_user_input()

            if ['yes', 'yeah', 'of course', 'offcourse','okay','sure','done'] in confirm.lower():
                server.sendmail(sender_email, recipient_email, email_message)
                server.quit()
                print("Sir, Email is sent successfully!")
            else:
                print("Email sending cancelled.")

        except Exception as e:
            print("An error occurred while sending the email:", e)
            print("Sorry, I couldn't send the email. Please try again.")
