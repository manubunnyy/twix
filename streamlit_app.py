import streamlit as st

# HTML and CSS for the transition effect and animation
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background-color: #f5f8fa;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      overflow: hidden;
    }

    .login-container {
      text-align: center;
    }

    h1 {
      font-size: 2.5rem;
      color: #1da1f2;
    }

    .button {
      display: inline-block;
      padding: 12px 24px;
      margin: 10px;
      background-color: #1da1f2;
      color: white;
      border: none;
      border-radius: 50px;
      font-size: 1.2rem;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    .button:hover {
      background-color: #1a91da;
    }

    .transition-screen {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: #1da1f2;
      z-index: 10;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.5s ease, visibility 0.5s ease;
    }

    .transition-screen.show {
      opacity: 1;
      visibility: visible;
    }

    @keyframes knife-sharpen {
      0% {
        clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
      }
      50% {
        clip-path: polygon(20% 0, 80% 0, 60% 100%, 40% 100%);
      }
      100% {
        clip-path: polygon(50% 0, 50% 0, 50% 100%, 50% 100%);
      }
    }

    .transition-screen.show {
      animation: knife-sharpen 0.5s forwards;
    }
  </style>
</head>
<body>
  <div class="login-container">
    <h1>Login to Twitter</h1>
    <button class="button" onclick="handleClick('login')">Login</button>
    <button class="button" onclick="handleClick('signup')">Sign Up</button>
  </div>

  <div class="transition-screen" id="transitionScreen"></div>

  <script>
    function handleClick(action) {
      document.getElementById("transitionScreen").classList.add("show");
      setTimeout(() => {
        window.location.href = action === 'login' ? '/login' : '/signup';
      }, 500); // Duration of the animation (500ms)
    }
  </script>
</body>
</html>
"""

# Streamlit app code
def main():
    st.title("Login Page")
    st.markdown(html_code, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
