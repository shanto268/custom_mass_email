# Custom Mass Emailer

This program can send custom emails en-masse using python's SMTP library.

## Installation

On your terminal, execute the following commands:

```
$ git clone 
$ cd custom_mass_email
$ pip install requirements.txt
```

Now that all the dependencies are installed. Replace the dummy fields in the `secrets.py` with your credentials and you are all set.

## Usage


### Only Emails

1. Create a `.csv` file with all the required emails and content elements for your email (see `example1.csv`)

2. Update the `email.xml` file with your desired email content and salutation. [**Make sure the dynamic fields match with the headers of the `.csv` fileyou created**]

3. $python SendEmails.py -i nameOfYourCsvFile.csv $

### Emails with Attachments

1. Create a `.csv` file with all the required emails and content elements for your email (see `example1.csv`)

2. Update the `email.xml` file with your desired email content and salutation. [**Make sure the dynamic fields match with the headers of the `.csv` fileyou created**]

3. Remember the pathway directory of your attachment.

4. $python SendEmails.py -i nameOfYourCsvFile.csv -a path/to/attachment $


## TO-DO:

-[  ] Add arguments and parsers

-[  ] Inputs

    -[  ] input csv

    -[  ] email content structure

        -[  ] body 

        -[  ] salutation

-[  ] Dynamic reading of csv headers

-[  ] Argument triggered email actions

    -[  ] Normal Email

    -[  ] Attachments
