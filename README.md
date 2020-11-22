# gofile

Package to access the gofile.io api.

The api is documented at https://gofile.io/api

## Usage

Uploading Files:

```
from gofile import GoUpload

f = GoUpload.create(["text.txt","image.png"],email = "name@email.com")

print(f.get_download_link())
print(f.ac)
```

Managing an Account

```
from gofile import GoAccount

a = GoAccount(token)

print(a.email)
print(a.files_count)
print(a.account)
print(a.files_size)
```

## Known Issues

- Deleting an Upload does not work.