if char in '0123456789.':
            current = self.text_input.get()
            # Clear input if operator is set and operand1 is already assigned
            if self.operator and (self.operand1 is not None) and (current == str(self.operand1)):
                current = ""
            self.text_input.set(current + char)
