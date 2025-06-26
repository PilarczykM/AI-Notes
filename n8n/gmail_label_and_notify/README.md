# 📬 Gmail Label & Notify Workflow

This n8n automation workflow fetches unread Gmail messages every 10 minutes, categorizes them using an AI model, and takes actions based on the classification — such as applying labels, deleting spam, and notifying users about job offers via Discord.

---

## 🔧 Features

- ⏱ **Scheduled Trigger**: Executes every 10 minutes.
- 📥 **Fetch Unread Emails**: Gets all unread Gmail messages.
- 🤖 **AI Categorization**:
  - Uses OpenAI (GPT-4o-mini) to classify each email based on subject and snippet.
  - Categories include:  
    - Personal  
    - Recruitment  
    - Social  
    - Rachunki (Bills)  
    - System Notifications  
    - Spam
- 🏷️ **Automated Labeling**:
  - Assigns Gmail labels to messages based on the AI-determined category.
- 🧹 **Spam Deletion**: Automatically deletes spam messages.
- ✅ **Read Marking**: Marks categorized messages as read after processing.
- 📣 **Job Notification via Discord**:
  - For recruitment emails, fetches the full message.
  - Uses OpenAI to summarize the job offer.
  - Posts a formatted summary to a specified Discord channel.

---

## 📌 Categories Explained

| Category                  | Description |
|--------------------------|-------------|
| **Personal**             | Private or personal emails unrelated to work. |
| **Recruitment**          | Job offers, HR outreach, and hiring announcements. |
| **Social**               | Social media platform updates (e.g., Facebook, LinkedIn). |
| **Rachunki (Bills)**     | Invoices, payment confirmations, and billing reminders. |
| **System Notifications** | Alerts from platforms, services, or security systems. |
| **Spam**                 | Irrelevant, suspicious, or mass advertisement emails. |

---

## 🔗 Integrations Used

- **Gmail**: For retrieving, labeling, reading, or deleting messages.
- **OpenAI**: For categorization and job offer summarization.
- **Discord Webhook**: For sending summarized job offers to a Discord channel.

---

## 🏁 How to Use

1. **Import the Workflow**  
   Open n8n and import the `gmail_label_and_notify.json` file.

2. **Set Up Credentials**  
   Ensure the following credentials are configured in n8n:
   - Gmail OAuth2
   - OpenAI API
   - Discord Webhook URL

3. **Configure Gmail Labels**  
   Make sure the label IDs used in the nodes match existing labels in your Gmail account. You may adjust them as needed.

4. **Enable the Workflow**  
   Activate the workflow to start automation every 10 minutes.

---

## 📝 Notes

- The job summary prompt is written in Polish, and the AI is expected to return structured recruitment info.
- Adjust label IDs or Discord formatting if using a different setup.

---

## 📄 License

This project is provided under the MIT License. You are free to use and adapt it for personal or commercial purposes.

