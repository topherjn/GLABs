from datetime import date
# Create a new Python file named "email_composer.py."
    # Done
# Define variables for recipient name, sender name, and a personalized message.
recipient_name = 'Joe'
sender_name = 'Lisa'

# Use string formatting to compose an email message.
# Experiment with including dynamic information, such as the current date.
message = 'Today is the {0:%d}th day of {0:%B}\nDear {1},' \
         '\nThank you for sending a mail.\nI really enjoyed it.' \
         '\nKind regards,\n{2}'.format(date.today(),recipient_name, sender_name)

# Print the results.
print(message)