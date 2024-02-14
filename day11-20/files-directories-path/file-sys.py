# with open("../../../../gitlab_vprofile_project/vprofile-project/Docker-files/app/Dockerfile") as file:
#     contents = file.read()
#     print(contents)

# with open("100_days_of_python/day11-20/files-directories-path/new_file.txt", mode="a") as file:
#     contents = file.write("This is another extra file to be added")
#     print(contents)

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
new_list = []

for number in a:
    if number % 2 == 0:
        new_list.append(number)
print(new_list)