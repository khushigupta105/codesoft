def chatbot(ipt){
  if ipt == "hello" or ipt =="hi ":
       return "hi , how are you?"
elif  ipt ==" how are you" or ipt=" i am fine ,how are you?" :
       return "I am great, how can i help you ?"
elif ipt=="set alaram at 6:00 AM ":
      return "Alaram set successfully!"
elif ipt=="thankyou":
      return "welcome"
}
ipt=input("user:")
if ipt =="bye:
    print("chatbot: Bye!")
else:
   answer=chatbot(ipt)
  print("chatbot:"answer)

