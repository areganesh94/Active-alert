import plivo

auth_id = "MAOGQ5ODNJYWZLZDNLOD"
auth_token = "NDU1ODZlNDQ1ZDFhYTY4MmQyMmUwMWJiNGM0N2U5"

p = plivo.RestAPI(auth_id, auth_token)

#Make_ call
params = {
    'from': '919442921464', # Caller Id
    'to' : '919901278850', # User Number to Call
#    'ring_url' : herokuapp /ring_url",
#    'answer_url' :/answer_url",
#    'hangup_url' :herukku url",
}
response = p.make_call(params)

# Also can add message & call record


