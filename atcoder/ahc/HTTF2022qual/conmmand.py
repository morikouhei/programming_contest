import subprocess
command = "cargo run --release --bin tester /Users/morikouhei/Documents/tools/dist/na < /Users/morikouhei/Documents/tools/in/0000.txt > out.txt".split(" ")

result = subprocess.run(command)
print(result)