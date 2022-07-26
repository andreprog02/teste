import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe

st.set_page_config(layout="centered", page_icon="🎓", page_title="Gerador")
st.title("🎓 Pra minha gatinha Gio!")

st.write(
    "Este app"
)

left, right = st.columns(2)

right.write("Aqui está o modelo que será utilizado:")

right.image("template.png", width=300)

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")


left.write("Fill in the data:")
form = left.form("template_form")
student = form.text_input("Seu nome")
course = form.selectbox(
    "Escolha uma opção",
    ["Sou uma gatinha", "Sou uma loirinha linda"],
    index=0,
)
grade = form.slider("Idade", 1, 100, 25)
submit = form.form_submit_button("Gerar PDF")

if submit:
    html = template.render(
        student=student,
        course=course,
        grade=f"{grade}/100",
        date=date.today().strftime("%B %d, %Y"),
    )

    pdf = pdfkit.from_string(html, False)
    st.balloons()

    right.success("🎉 Seu Documento está gerado!")
    # st.write(html, unsafe_allow_html=True)
    # st.write("")
    right.download_button(
        "⬇️ Download PDF",
        data=pdf,
        file_name="diploma.pdf",
        mime="application/octet-stream",
    )
