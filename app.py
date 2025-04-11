import streamlit as st
import math

def calculate_current_percentage(total_classes, attended_classes):
    if total_classes == 0:
        return 0
    return (attended_classes / total_classes) * 100

def calculate_classes_needed(total_classes, attended_classes, desired_percentage):
    if desired_percentage <= 0:
        return 0
    if desired_percentage >= 100:
        return "all remaining"
    
    required_classes = (desired_percentage * total_classes - 100 * attended_classes) / (100 - desired_percentage)
    return max(0, required_classes)

def main():
    st.title("📊 Attendance Percentage Calculator")
    st.write("Calculate your current attendance percentage or find out how many more classes you need to attend to reach your desired percentage.")
    
    # Input fields
    col1, col2 = st.columns(2)
    with col1:
        total_classes = st.number_input("Total Classes Held", min_value=0, step=1, value=0)
    with col2:
        attended_classes = st.number_input("Classes Attended", min_value=0, step=1, value=0)
    
    # Validate input
    if attended_classes > total_classes:
        st.error("Attended classes cannot be more than total classes held!")
        return
    
    # Current attendance display
    current_percentage = calculate_current_percentage(total_classes, attended_classes)
    st.subheader(f"Current Attendance: {current_percentage:.2f}%")
    
    # Buttons for actions
    st.markdown("---")
    st.subheader("Attendance Target Calculator")
    
    desired_percentage = st.slider(
        "Select your desired attendance percentage",
        min_value=0.0,
        max_value=100.0,
        value=75.0,
        step=0.1
    )
    
    if st.button("Calculate Classes/Days Needed for Target"):
        if desired_percentage < 0 or desired_percentage > 100:
            st.error("Percentage must be between 0 and 100")
        else:
            if current_percentage >= desired_percentage:
                st.success(f"🎉 You already have {current_percentage:.2f}% attendance which meets your target of {desired_percentage}%!")
            else:
                classes_needed = calculate_classes_needed(total_classes, attended_classes, desired_percentage)
                
                if isinstance(classes_needed, str):
                    st.info("You need to attend all remaining classes to reach 100%")
                else:
                    # Assuming 6 classes per day
                    days_needed = classes_needed / 6
                    
                    st.success(
                        f"To reach {desired_percentage}% attendance from your current {current_percentage:.2f}%:\n\n"
                        f"📚 **Classes needed:** {math.ceil(classes_needed)} more classes\n"
                        f"📅 **Days needed:** {math.ceil(days_needed)} days (assuming 6 classes per day)\n\n"
                        f"🔹 *This means you should attend all classes for the next {math.ceil(days_needed)} days*"
                    )

    # Footer with clickable developer name
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; padding: 10px;">
            Developed by <a href="https://mdwaseel.bewebfy.com/" >Waseel</a>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()