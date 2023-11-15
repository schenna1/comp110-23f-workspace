"""Class to store a message (operator overload, union types, default parameters)."""

class Message:

#to can be string or int
    to: str | int
    content: str
    important: bool

#default importance is False
    def __init__(self, recipient: str | int, message_content: str, importance_flag: bool = False) -> None:
        """Construct a message."""
        self.to = recipient
        self.content = message_content
        self.important = importance_flag

    def __str__(self) -> str:
        output: str = f"Message to {self.to}:\n"
        output += f"Important? {self.important}\n"
        output += f'"{self.content}"'
        return output
    
    #operator overload
    def __mul__(self, factor: int):
        """Multiplication Operator overload."""
        copy_val: str = self.content
        for loop_number in range(1, factor):
            self.content += " " + copy_val

msg: Message = Message("erin", "Great job!", False)
#to multiply message 100x: msg * 100
print(msg)

    
