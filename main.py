import streamlit as st
from decimal import Decimal, getcontext

getcontext().prec = 10
def fixed_point_addition(a: Decimal, b: Decimal) -> Decimal:
    return a + b
def floating_point_addition(a: float, b: float) -> float:
    return a + b
def create_karnaugh_map(minterms):
    k_map = [['0', '0'], ['0', '0']]
    for m in minterms:
        if m == 0:
            k_map[0][0] = '1'
        elif m == 1:
            k_map[0][1] = '1'
        elif m == 2:
            k_map[1][0] = '1'
        elif m == 3:
            k_map[1][1] = '1'
    return k_map

# Function for RS Flip-Flop
class RSFlipFlop:
    def __init__(self):
        self.Q = 0
        self.Q_not = 1

    def set(self):
        self.Q = 1
        self.Q_not = 0

    def reset(self):
        self.Q = 0
        self.Q_not = 1

    def get_state(self):
        return self.Q, self.Q_not

# Streamlit app
def main():
    st.title("Dynamic Data Input and Problem Solver")

    # Fixed-point and Floating-point number inputs
    st.header("Fixed-Point and Floating-Point Addition")
    fixed_a = st.number_input("Enter fixed-point number (Decimal) A:", value=0.0, format="%.2f", key="fixed_a")
    fixed_b = st.number_input("Enter fixed-point number (Decimal) B:", value=0.0, format="%.2f", key="fixed_b")
    float_a = st.number_input("Enter floating-point number A:", value=0.0, key="float_a")
    float_b = st.number_input("Enter floating-point number B:", value=0.0, key="float_b")

    if st.button("Calculate Fixed-Point Sum"):
        fixed_sum = fixed_point_addition(Decimal(fixed_a), Decimal(fixed_b))
        st.success(f"Fixed-point addition result: {fixed_sum}")

    if st.button("Calculate Floating-Point Sum"):
        float_sum = floating_point_addition(float_a, float_b)
        st.success(f"Floating-point addition result: {float_sum}")

    # Karnaugh Map input
    st.header("Karnaugh Map Generator")
    minterms_input = st.text_input("Enter minterms (comma-separated):", key="minterms_input")
    if minterms_input:
        minterms = list(map(int, minterms_input.split(',')))
        k_map = create_karnaugh_map(minterms)
        st.write("Karnaugh Map:")
        st.table(k_map)

    # RS Flip-Flop simulation
    st.header("RS Flip-Flop Simulation")
    flip_flop = RSFlipFlop()
    if st.button("Set Flip-Flop"):
        flip_flop.set()
        st.success("Flip-Flop set!")
    if st.button("Reset Flip-Flop"):
        flip_flop.reset()
        st.success("Flip-Flop reset!")

    st.write(f"Current State of Flip-Flop: Q = {flip_flop.get_state()[0]}, Q' = {flip_flop.get_state()[1]}")

if __name__ == "__main__":
    main()
