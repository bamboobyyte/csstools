# CSSTools 💻

Welcome to `CSSTools`, a toolbox crafted for CSS support engineers to streamline their workflows! 🛠️ This Flask-based web application is designed to be accessible and easy to deploy, ensuring that you can focus on what's most important—supporting and enhancing CSS functionalities.

## Deployment 🚀

To get `CSSTools` up and running:

1. **Setup Environment**:

   - Recommend using a virtual environment to isolate package dependencies. Use the following command to create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     ```bash
     source venv/bin/activate  # On Unix/macOS
     .\venv\Scripts\activate  # On Windows
     ```

2. **Install Dependencies**:

   - Install the required packages with:
     ```bash
     pip install -r requirements.txt
     ```

3. **Setting up Environment Variables**:

   - Make a copy of .env.template
     ```bash
     cp .env.template .env
     ```

4. **Running the Application**:

   - Launch the Flask application by:
     ```bash
     python app.py
     ```

5. **Accessing the Application**:
   - After deployment, access the web interface through your browser at `http://localhost:5000` or configure as per the next steps for production use.

## Nginx Reverse Proxy Setup 🔒

For public accessable environments, it’s highly recommended to use Nginx as a reverse proxy to add an additional layer of security:

- **Nginx Configuration** (Highly Recommended ❗):

  - Configure Nginx to forward requests to your Flask application.
  - Consider adding basic authentication or client certificate authentication for additional security, as this Flask app does not include an authentication method by default.

- **System Service** (Optional):
  - For Linux users, you can set up the application as a service for auto-start capabilities.

## Compatibility 📐

Tested primarily on Ubuntu, `CSSTools` is built with Flask, making it potentially compatible with other operating systems that support Python.

## Contributing 🤝

Contributions to `CSSTools` are welcome! If you have suggestions or improvements, feel free to fork the repo and submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

We hope `CSSTools` enhances your efficiency and simplifies your CSS-related tasks!
