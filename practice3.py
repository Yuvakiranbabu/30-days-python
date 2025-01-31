#sending message to different people

people=["Jonah","Chandler","Jim","Phil"]
their_msg={"jonah":"welcome to cloud9",
"chandler":"welcome to friends reunion","jim":"welcome to the office","phil":"welcome to the modern family"}


def sitcom_mail():
    for i in people:
        for j in their_msg:
            if i.lower()==j:
                print("hey ",j," ",their_msg[j])


sitcom_mail()