import streamlit as st

st.set_page_config(
    page_title="Number Statistics",
    page_icon="🔢",
    layout="centered"
)

st.title("🔢 Number Statistics")

st.write(
    "Enter numbers to identify even and odd numbers "
    "and find the largest and smallest values."
)

numbers_input = st.text_input(
    "Enter numbers separated by spaces",
    "12 7 25 4 18 9 31 6 15 20"
)

if st.button("Analyze Numbers"):

    try:
        numbers = list(map(int, numbers_input.split()))

        if not numbers:
            st.warning("Please enter at least one number.")
        else:
            even_numbers = []
            odd_numbers = []

            for number in numbers:
                if number % 2 == 0:
                    even_numbers.append(number)
                else:
                    odd_numbers.append(number)

            largest = max(numbers)
            smallest = min(numbers)

            st.subheader("Results")

            st.write("**Original Numbers:**", numbers)
            st.write("**Even Numbers:**", even_numbers)
            st.write("**Odd Numbers:**", odd_numbers)
            st.write("**Largest Number:**", largest)
            st.write("**Smallest Number:**", smallest)

    except ValueError:
        st.error("Please enter valid numbers separated by spaces.")