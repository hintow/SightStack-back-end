# SightStack-back-end

## Back End

The back-end repository provides the API to fetch words for the specific game level, with data stored in a database.

### Features:
- RESTful API to retrieve a list of words for a specific level.
- API endpoints to interact with the front end and provide necessary data for the game.
- Database for storing and retrieving words and level information.

### Tech Stack:
- **Flask**: Python web framework for building the API.
- **PostgreSQL**: Database for storing words and level information.
- **SQLAlchemy**: ORM for interacting with the database.

### Tables and Relationships:

#### Users Table:
- Stores user-related information (id, username, password_hash, avatar).
- **Primary Key**: id.
- Has a one-to-many relationship with user_achievements and games.

#### User Achievements Table:
- Tracks achievements for each user.
- **Fields**: achievement_id (Primary Key), user_id (Foreign Key to users.id), description.
- Linked to the users table via user_id.

#### Games Table:
- Represents game instances played by users.
- **Fields**: id (Primary Key), user_id (Foreign Key to users.id), score.
- Linked to the users table via user_id.

#### Words Table:
- Stores words for the game.
- **Fields**: id (Primary Key), word, grade, description.
- Serves as a word bank for the game.

#### Games_Words Table:
- Many-to-many relationship between games and words.
- **Fields**: game_id (Foreign Key to games.id), word_id (Foreign Key to words.id).

### MVP:

#### Starting a New Game:
When a user starts a new round of the game:
- A new record is created in the games table (let's call this the round ID).
- The user's selected level is used to filter words from the words table (e.g., by grade or another level-related attribute).
- Five words are randomly selected from this filtered set.

#### Updating games_words Table:
For each of the five words selected, a new record is added to the games_words table to associate the selected words with the newly created game/round ID.

#### Returning the Response:
The API returns:
- The round ID from the games table.
- The five selected words (their word values).
- Their definitions (the description field from the words table).

### Setup Instructions:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/hintow/SightStack-back-end
    cd SightStack-back-end
    ```

2. **Create a virtual environment and activate it**:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    - Ensure PostgreSQL is installed and running.
    - Create a database named `sightstack_dev`.
    - Update the `SQLALCHEMY_DATABASE_URI` in the [.env](http://_vscodecontentref_/0) file with your database credentials.

5. **Run the migrations**:
    ```sh
    flask db upgrade
    ```

6. **Start the Flask application**:
    ```sh
    flask run --debug
    ```

### Running Tests:

1. **Run the tests**:
    ```sh
    pytest
    ```

### API Endpoints:

- **GET /words/level/<level>**: Retrieve a list of words for a specific level.
- **POST /register**: Register a new user.
- **POST /login**: Login a user.

### Contributing:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

### License:

This project is licensed under the MIT License - see the LICENSE file for details.