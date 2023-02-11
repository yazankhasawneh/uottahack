import pandas as pd
import cohere
from cohere.classify import Example

api_key = "UtsZMr3FKeydAs2M6CgLaE664rTTh9I0rJrqmSLA"
co = cohere.Client(api_key)


user_input = input("How can I help you today? ")
inputs=[user_input.lower()]

examples=[
  Example("heart pain", "cardiovascular problem"),
  Example("heartache", "cardiovascular problem"),
  Example("heart beats fast", "cardiovascular problem"),
  Example("fever", "cold"),
  Example("headache", "cold"),
  Example("stuffy nose", "cold"),
  Example("runny nose", "cold"),
  Example("runny nose", "flu"),
  Example("joint pain", "cold"),
  Example("thirsty", "cold"),
  Example("thirsty", "flu"),
  Example("loss of appetite", "cold"),
  Example("loss of appetite", "flu")
]

response = co.classify(
  inputs=inputs,
  examples=examples,
)

print(response.classifications)