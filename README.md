# jobs-scrapper

Jobs Scrapper for LinkedIn and Indeed

## Configuration

The `config.json` file contains the configuration options for the scraper and the web interface. Below is a description of each option:

- `proxies`: The proxy settings for the requests library. Set the `http` and `https` keys with the appropriate proxy URLs.
- `headers`: The headers to be sent with the requests. Set the `User-Agent` key with a valid user agent string. If you don't know your user agen, google "my user agent" and it will show it.
- `OpenAI_API_KEY`: Your OpenAI API key. You can get it from your OpenAI dashboard.
- `OpenAI_Model`: The name of the OpenAI model to use for cover letter generation. GPT-4 family of models produces best results, but also the most expensive one.
- `resume_path`: Local path to your resume in PDF format (only PDF is supported at this time). For best results it's advised that your PDF resume is formatted in a way that's easy for the AI to parse. Use a single column format, avoid images. You may get unpredictable results if it's in a two-column format.
- `search_queries`: An array of search query objects, each containing the following keys:
  - `keywords`: The keywords to search for in the job title.
  - `location`: The location to search for jobs.
  - `f_WT`: The job type filter. Values are as follows: - 0 - onsite - 1 - hybrid - 2 - remote - empty (no value) - any one of the above.
- `desc_words`: An array of keywords to filter out job postings based on their description.
- `title_include`: An array of keywords to filter job postings based on their title. Keep _only_ jobs that have at least one of the words from 'title_words' in its title. Leave empty if you don't want to filter by title.
- `title_exclude`: An array of keywords to filter job postings based on their title. Discard jobs that have ANY of the word from 'title_words' in its title. Leave empty if you don't want to filter by title.
- `company_exclude`: An array of keywords to filter job postings based on the company name. Discard jobs come from a certain company because life is too short to work for assholes.
- `languages`: Script will auto-detect the language from the description. If the language is not in this list, the job will be discarded. Leave empty if you don't want to filter by language. Use "en" for English, "de" for German, "fr" for French, "es" for Spanish, etc. See documentation for langdetect for more details.
- `timespan`: The time range for the job postings. "r604800" for the past week, "r84600" for the last 24 hours. Basically "r" plus 60 _ 60 _ 24 \* <number of days>.
- `jobs_tablename`: The name of the table in the SQLite database where the job postings will be stored.
- `filtered_jobs_tablename`: The name of the table in the SQLite database where the filtered job postings will be stored.
- `db_path`: The path to the SQLite database file.
- `pages_to_scrape`: The number of pages to scrape for each search query.
- `rounds`: The number of times to run the scraper. LinkedIn doesn't always show the same results for the same search query, so running the scraper multiple times will increase the number of job postings scraped. I set up a cron job that runs every hour during the day.
- `days_toscrape`: The number of days to scrape. The scraper will ignore job postings older than this number of days.
