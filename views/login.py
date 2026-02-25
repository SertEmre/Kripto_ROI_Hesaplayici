import streamlit as st
import core.data_manager as data_manager
import time 

st.markdown("""
<style>
    /* Ana arka plan (Görseldeki koyu ton) */
    .stApp {
        background-color: #0E0E0E;
    }
    
    /* --- Input (Giriş Kutuları) Tasarımı --- */
    .stTextInput input {
        background-color: #1E1E1E !important; 
        color: #E0E0E0 !important; 
        border: 1px solid #333 !important; 
        border-radius: 10px !important; 
        padding: 15px !important; 
    }
    .stTextInput input:focus {
        border-color: #C6934B !important;
        box-shadow: 0 0 5px rgba(198, 147, 75, 0.5) !important;
    }
    
    /* --- Yazı Renkleri --- */
    .stTextInput label, p, h1, h2, h3 {
        color: #F0F0F0 !important; 
    }

    /* --- BUTON TASARIMI --- */
    .stButton > button {
        width: 100%;
        background-color: #C6934B !important; 
        color: #000000 !important; 
        font-weight: 800 !important; 
        font-size: 16px !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 15px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 10px rgba(198, 147, 75, 0.3) !important;
    }
    
    .stButton > button:hover {
        background-color: #B07D3A !important; 
        box-shadow: 0 6px 15px rgba(198, 147, 75, 0.5) !important;
        transform: translateY(-2px); 
    }
    
    /* --- Sekme (Tab) Tasarımı --- */
    .stTabs [data-baseweb="tab-list"] {
        gap: 25px;
        border-bottom: 2px solid #333;
    }
    .stTabs [data-baseweb="tab"] {
        color: #888; 
        font-weight: bold;
        border: none !important;
        padding-bottom: 10px;
    }
    .stTabs [aria-selected="true"] {
        color: #C6934B !important;
        border-bottom: 3px solid #C6934B !important;
    }
</style>
""", unsafe_allow_html=True)

col_bosluk1, col_ana, col_bosluk2 = st.columns([1.5, 5, 1.5])

with col_ana:
    st.write("<br><br>", unsafe_allow_html=True) 
    
    col_sol, col_sag = st.columns([1.1, 1], gap="medium")
    
    with col_sol:
        try:
            st.image("assets/bg.jpg", use_container_width=True)
        except:
            st.warning("assets klasörünün içine 'bg.jpg' adında bir resim koymalısın.")
            
    with col_sag:
        st.write("<div style='padding-left: 20px;'>", unsafe_allow_html=True)
        
        st.markdown("<h2 style='margin-top:0;'>Hesabını Oluştur</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: gray !important; margin-bottom: 25px;'>Yatırımlarını profesyonelce yönetmeye hemen başla.</p>", unsafe_allow_html=True)
        
        tab_kayit, tab_giris = st.tabs(["Kayıt Ol", "Giriş Yap"])
        
        with tab_kayit:
            st.write("<br>", unsafe_allow_html=True)
            reg_user = st.text_input("Kullanıcı Adı", key="r_user", placeholder="Adınızı girin")
            reg_pass = st.text_input("Şifre", type="password", key="r_pass", placeholder="Güçlü bir şifre seçin")
            reg_pass2 = st.text_input("Şifre (Tekrar)", type="password", key="r_pass2", placeholder="Şifrenizi doğrulayın")
            st.write("<br>", unsafe_allow_html=True)
            sartlar = st.checkbox("Şartları ve Koşulları kabul ediyorum.")
            
            st.write("<br>", unsafe_allow_html=True)
            if st.button("Kayıt Ol", key="btn_reg"):
                if not sartlar:
                    st.warning("Şartları kabul etmelisiniz.")
                elif reg_pass != reg_pass2:
                    st.error("Şifreler uyuşmuyor!")
                elif len(reg_user) > 2 and len(reg_pass) > 2:
                    basarili, mesaj = data_manager.register_user(reg_user, reg_pass)
                    if basarili:
                        st.success("Kayıt başarılı! Oturum açılıyor...")
                        time.sleep(1) 
                        st.session_state['kullanici'] = reg_user 
                        st.rerun() 
                    else:
                        st.error(mesaj)
                else:
                    st.warning("Kullanıcı adı ve şifre en az 3 karakter olmalıdır.")
                    
        with tab_giris:
            st.write("<br>", unsafe_allow_html=True)
            login_user = st.text_input("Kullanıcı Adı", key="l_user", placeholder="Kullanıcı adınız")
            login_pass = st.text_input("Şifre", type="password", key="l_pass", placeholder="Şifreniz")
            
            st.write("<br><br>", unsafe_allow_html=True)
            if st.button("Giriş Yap", key="btn_login"):
                if data_manager.verify_user(login_user, login_pass):
                    st.session_state['kullanici'] = login_user
                    st.rerun()
                else:
                    st.error("Hatalı kullanıcı adı veya şifre!")
                    
        st.write("</div>", unsafe_allow_html=True)