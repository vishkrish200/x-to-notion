# x-to-notion

**x-to-notion** is a tool designed to export your Twitter (formerly known as "X") bookmarks directly to Notion, helping you organize and manage your saved tweets efficiently in a Notion database.

## Features

- **Twitter Bookmark Export**: Export all your bookmarked tweets from Twitter to a Notion database.
- **Automated Workflow**: Set up periodic exports of your bookmarks to Notion, keeping everything up-to-date.
- **Customizable Mapping**: Adjust how tweet information (text, media, links, etc.) is stored in Notion.

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/en/) (version 14 or higher)
- Twitter API credentials (Get from [Twitter Developer Portal](https://developer.twitter.com/en/docs))
- Notion API key (See [Notion API documentation](https://developers.notion.com/) to generate one)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/vishkrish200/x-to-notion.git
    ```

2. Navigate into the project directory:

    ```bash
    cd x-to-notion
    ```

3. Install dependencies:

    ```bash
    npm install
    ```

4. Set up your environment variables by creating a `.env` file:

    ```bash
    touch .env
    ```

    Add the following environment variables to the `.env` file:

    ```bash
    TWITTER_API_KEY=your_twitter_api_key
    TWITTER_API_SECRET=your_twitter_api_secret
    TWITTER_ACCESS_TOKEN=your_twitter_access_token
    TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
    NOTION_API_KEY=your_notion_api_key
    NOTION_DATABASE_ID=your_notion_database_id
    ```

### Usage

After setting up, run the script to export your Twitter bookmarks to your Notion database:

```bash
node index.js
```

### Example

By running the script, your bookmarked tweets will automatically be added to your specified Notion database. The information saved includes:

- Tweet content
- Tweet URL
- Associated media (if available)

You can customize how this information is stored by adjusting the mapping in `config.js`.

### Configuration

- `config.js` allows you to customize how Twitter bookmark data is stored in Notion. You can modify:
    - **Field mapping**: Adjust how tweet content, URLs, and media are mapped to Notion properties.
    - **Notion database**: Change the target Notion database ID.

## Troubleshooting

- **Invalid API keys**: Ensure that your Twitter and Notion API credentials are correct and have sufficient permissions.
- **Network issues**: Verify that both Twitter and Notion APIs are accessible from your environment.

## Contributing

Contributions are welcome! If you'd like to contribute, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.
