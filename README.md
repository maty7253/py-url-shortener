# URL Shortener

A simple URL shortener built with Flask and SQLite. This project allows users to create shortened URLs and track their usage statistics.

## Features

- Shorten long URLs to manageable lengths
- Track click statistics for each shortened URL
- View creation date and total clicks for each URL
- Clean and responsive user interface
- SQLite database for persistent storage

## Installation

1. Clone the repository:
```bash
git clone https://github.com/maty7253/py-url-shortener.git
cd url-shortener
```


2. Create a virtual environment and activate it:
```shellscript
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```shellscript
pip install -r requirements.txt
```

## Usage

1. Start the application:
```shellscript
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`
3. Enter a URL to shorten it
4. View statistics at `http://localhost:5000/stats`


## Project Structure

```plaintext
url-shortener/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── urls.db            # SQLite database (created automatically)
└── templates/         # HTML templates
    ├── index.html     # Home page template
    └── stats.html     # Statistics page template
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request


## License

This project is licensed under the MIT License - see the LICENSE file for details.


<hr/>


This URL shortener project includes:

1. A Flask web application (`app.py`) that handles:
   - URL shortening
   - Redirect functionality
   - Click tracking
   - Statistics viewing

2. Two HTML templates with a clean, responsive design using Tailwind CSS:
   - `index.html` for the main URL shortening interface
   - `stats.html` for viewing URL statistics

3. A SQLite database to store:
   - Original URLs
   - Short codes
   - Creation timestamps
   - Click counts

4. A comprehensive README.md file for GitHub

To get started with this project:

1. Create a new GitHub repository
2. Copy these files into your repository
3. Follow the installation instructions in the README
4. Push the code to GitHub

The application features:
- Clean and intuitive user interface
- Input validation
- Click tracking
- Statistics page
- Responsive design
- Secure random short code generation
- Automatic database initialization

You can extend this project by adding features like:
- User authentication
- Custom short codes
- API endpoints
- QR code generation
- Link expiration
- Analytics dashboard
