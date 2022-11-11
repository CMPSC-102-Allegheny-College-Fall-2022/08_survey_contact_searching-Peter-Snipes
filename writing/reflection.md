# Contact Searching

Make sure that you delete all of the markers and the written prompts
from this document. You should also ensure that the document does not have any
mistakes in spelling, grammar, or the syntax of Markdown. Ultimately, the final
version of your reflection should be a polished document that is suitable for
publication on your web site.

## Peter Snipes

## Program Output

### What is the output from running the following commands?

```

```

Use a fenced code block to provide the output for this command.

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

```

```

Use a fenced code block to provide the output for this command.

- `poetry run contactsearcher --job-description "neer" --contacts-file input/contacts.txt`

## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### The source code statement that makes the `search` module available to `main`

```

```

Use a fenced code block to provide the requested source code
Write at least one paragraph to explain the request source code

#### The source code statement that extracts the current job description for a contact

```

```

Use a fenced code block to provide the requested source code
Write at least one paragraph to explain the request source code

#### Invocation of the function called `search_for_email_given_job`

```

```

Use a fenced code block to provide the requested source code
Write at least one paragraph to explain the request source code

#### Test case for the function called `search_for_email_given_job`

```

```
This code is a test case that is searching for a given job. The g=job thats given in this
example is a "nurse" so if one of the peoples jobs are a nurse the test case will come back true.

Use a fenced code block to provide the requested source code
Write at least one paragraph to explain the request source code

#### Execute trace of the `contactsearcher` program

When running the "contactsearcher" function you are basically searching through all theinformation in the database where the emails and job titles are stored. When searching
through it you have the option to search for a specific person throught their job description. "contactsearcher --job-description "engineer" --contacts-file" This is looking for engineers and itll print out that persons email.

Explain each function call that takes place for the following run of the program
Write at least one paragraph to explain every function call when running `contactsearcher`

Your discussion should start with the invocation of the `contactsearcher`
function in the `main` module, explain all of the subsequent function calls in
the correct order, and then show how the program's control returns to the
`contactsearcher` function in the `main` module.

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

## Professional Assessment

### So far this semester, what is one area in which you have struggled? How did you overcome this challenge?

One area I struggled with is with docker, poetry, and things that allow me to run my code
to check it. I've overcame this by uninstalling and trouble shooting them. I've also struggled with some things with pythons language but getting help from TA's has helped me gain a better understanding of what I am learning in class.

Provide a one-paragraph response that answers this question in your own words.

### Based on your experiences with this project, what is one way in which you want to improve?

One way I want to improve is my overall understanding of python language and I want to
better my implementation of coding.

Provide a one-paragraph response that answers this question in your own words.
