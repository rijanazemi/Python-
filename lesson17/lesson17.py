import streamlit as st

st.title("Hello, World with Streamlit!")
st.write("Welcome to the Streamlit app")

if st.button('Click Me'):
    st.write('Button clicked!')
    st.checkbox("check me")

if st.checkbox("check me to show some text"):
    # If checkbox is checked, display the text
    st.write("hello digitalschool")

    user_input = st.text_input("Enter text", "Enter some text here")
    st.write("You Entered:", user_input)

    age = st.number_input("Enter your age", min_value=1, max_value=100)
    st.write(f'Your age: {age}')

    message = st.text_area("Enter a message")
    st.write(f"Your message: {message}")

    choice = st.radio("Pick one", ['Choice 1', 'Choice 2', 'Choice 3'])  # Corrected the typo here
    st.write(f"You chose: {choice}")

    if st.button("Success"):
        st.success("It was sent successfully")

        try:
            1 / 0
        except Exception as e:
            st.exception(e)

# The calculator functions and main logic should be defined outside the button condition
def calculate(num1, num2, operation):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Error! Division by zero."

def main():
    st.title("Simple Calculator")

    st.header("Enter Numbers for Calculation")
    num1 = st.number_input("Enter the first number", value=0)
    num2 = st.number_input("Enter the second number", value=0)

    operation = st.selectbox("Select Operation", ("Add", "Subtract", "Multiply", "Divide"))

    if st.button("Calculate"):
        result = calculate(num1, num2, operation)
        st.write(f"The result of {operation}ing {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()