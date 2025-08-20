# 📧 Mailgun Bulk Email Sender (Python + CSV + HTML)

Send personalized HTML emails to a list of recipients using Mailgun’s API and pure Python — no frameworks needed.

---

## ✅ Features

- Send bulk emails using a `recipients.csv` file
- Personalize each email using names (`Hi John!`)
- Send rich HTML emails
- Mailgun open/click tracking enabled
- Error handling + retry logic built in

---

## 🗂️ Project Structure



✅ Step 4: How to Add DNS Records for Mailgun
📌 What You Need First:

    A domain name (from Namecheap, GoDaddy, Google Domains, etc.)

    A Mailgun account

🪜 Step-by-Step Guide:

    Login to Mailgun
    → Go to Mailgun Dashboard

    Add a Domain
    Click “Add New Domain”
    Use a subdomain like: mg.yourdomain.com

    Mailgun shows you DNS Records
    You’ll see:

        2 × TXT records

        2 × MX records

        1 × CNAME record

    Go to your domain provider’s DNS panel
    (e.g. Namecheap, GoDaddy, etc.)

    Copy-paste the records exactly

        Type: TXT / MX / CNAME

        Host: might be mg, or mg.yourdomain.com depending on provider

        Value: Mailgun gives you this

    Save changes
    Wait ~15–60 minutes for Mailgun to detect them.

    Go back to Mailgun → Click "Check DNS Records"
    When all are ✅ verified, your domain is ready!

🧪 After that:

    Plug your domain & API key into the script

    Start sending emails 🎉



| Rank  | Service           | Why Recommended                                                              |
| ----- | ----------------- | ---------------------------------------------------------------------------- |
| **1** | **Resend**        | Super simple UI, fast signup, 3,000 emails/month free, modern API            |
| **2** | **MailerSend**    | Very developer-friendly, generous free tier (3,000/month), easy setup        |
| **3** | **Elastic Email** | Simple REST API, 100 emails/day free, very low paid rates (\$0.09/1k emails) |
| **4** | **Mailjet**       | 6,000 emails/month (200/day), decent API, account approval usually fast      |
| **5** | **SMTP2GO**       | 1,000/month free, fast signup, good reliability, easy API                    |
