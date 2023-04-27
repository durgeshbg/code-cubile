document.addEventListener("DOMContentLoaded", function () {
    // Use buttons to toggle between views
    document
        .querySelector("#inbox")
        .addEventListener("click", () => load_mailbox("inbox"));
    document
        .querySelector("#sent")
        .addEventListener("click", () => load_mailbox("sent"));
    document
        .querySelector("#archived")
        .addEventListener("click", () => load_mailbox("archive"));
    document
        .querySelector("#compose")
        .addEventListener("click", () => compose_email({}));

    // Post mail
    document.querySelector("form").addEventListener("submit", send_mail);

    // By default, load the inbox
    load_mailbox("inbox");
});

function compose_email(reply) {
    // Show compose view and hide other views
    document.querySelector("#emails-view").style.display = "none";
    document.querySelector("#mail-view").style.display = "none";
    document.querySelector("#compose-view").style.display = "block";

    if (Object.keys(reply).length === 0) {
        // Clear out composition fields
        document.querySelector("#compose-recipients").value = "";
        document.querySelector("#compose-subject").value = "";
        document.querySelector("#compose-body").value = "";
    } else {
        document.querySelector("#compose-recipients").value = `${reply.sender}`;
        let subject = reply.subject;
        if (!subject.includes("Re: ")) {
            subject = "Re: " + subject;
        }
        document.querySelector("#compose-subject").value = subject;
        document.querySelector(
            "#compose-body"
        ).value = `On ${reply.timestamp} ${reply.sender} wrote: ${reply.body}`;
    }
}

function load_mailbox(mailbox) {
    // Show the mailbox and hide other views
    document.querySelector("#emails-view").style.display = "block";
    document.querySelector("#mail-view").style.display = "none";
    document.querySelector("#compose-view").style.display = "none";

    // Show the mailbox name
    document.querySelector("#emails-view").innerHTML = `<h3>${
        mailbox.charAt(0).toUpperCase() + mailbox.slice(1)
    }</h3>`;

    fetch(`emails/${mailbox}`)
        .then((response) => response.json())
        .then((data) => {
            data.forEach((contents) => {
                const emails_view = document.querySelector("#emails-view");
                const mail = document.createElement("div");
                mail.innerHTML = `<div>From: ${contents.sender}</div>`;
                mail.innerHTML += `<div>Subject: ${contents.subject}</div>`;
                mail.innerHTML += `<div>Time: ${contents.timestamp}</div>`;
                mail.classList.add("mail");
                if (contents.read) {
                    mail.classList.add("read");
                }
                emails_view.append(mail);
                mail.addEventListener("click", () => {
                    mail_view(contents.id, mailbox);
                });
            });
        });
}

function send_mail(event) {
    const cmpRecipients = document.querySelector("#compose-recipients").value;
    const cmpSubject = document.querySelector("#compose-subject").value;
    const cmpBody = document.querySelector("#compose-body").value;

    event.preventDefault();
    fetch("/emails", {
        method: "POST",
        body: JSON.stringify({
            recipients: cmpRecipients,
            subject: cmpSubject,
            body: cmpBody,
        }),
    })
        .then((response) => response.json())
        .then((result) => {
            if (result.error) {
                document.querySelector("#error").innerHTML = result.error;
            } else {
                load_mailbox("sent");
            }
        });
}

function mail_view(id, mailbox) {
    document.querySelector("#emails-view").style.display = "none";
    document.querySelector("#mail-view").style.display = "block";
    document.querySelector("#compose-view").style.display = "none";

    fetch(`emails/${id}`, {
        method: "PUT",
        body: JSON.stringify({
            read: true,
        }),
    });

    const mail_view = document.querySelector("#mail-view");
    fetch(`emails/${id}`)
        .then((response) => response.json())
        .then((data) => {
            // Loading mail with data
            mail_view.innerHTML = `<div><b>From:</b> ${data.sender}</div>`;
            mail_view.innerHTML += `<div><b>To:</b> ${data.recipients}</div>`;
            mail_view.innerHTML += `<div><b>Subject:</b> ${data.subject}</div>`;
            mail_view.innerHTML += `<div><b>Body:</b> ${data.body}</div>`;
            mail_view.innerHTML += `<div><b>Time:</b> ${data.timestamp}</div>`;
            mail_view.innerHTML += `<div><button class="reply">Reply</button></div>`;

            // Add the archive button by checking which box the user is in
            if (mailbox !== "sent") {
                if (!data.archived) {
                    mail_view.innerHTML += `<div><button class="archive">Archive</button></div>`;
                } else {
                    mail_view.innerHTML += `<div><button class="archive">Unarchive</button></div>`;
                }
            }

            // Listening to archive event
            document.querySelector(".archive").addEventListener("click", () => {
                fetch(`emails/${data.id}`, {
                    method: "PUT",
                    body: JSON.stringify({
                        archived: !data.archived,
                    }),
                });
                load_mailbox("inbox");
            });
            // Listening to reply event
            document
                .querySelector(".reply")
                .addEventListener("click", () => compose_email(data));
        });
}
