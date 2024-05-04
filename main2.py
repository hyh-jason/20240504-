import sys

if __name__ == '__main__':
    while True:
        input_str = sys.stdin.readline().strip()
        if input_str == '':
            break

        output_str = ''

        st = []
        for i in range(len(input_str)):
            if input_str[i] == ')':
                if len(st) > 0 and st[-1][0] == '(':
                    st.pop()
                    output_str += ' '
                else:
                    output_str += '?'
            elif input_str[i] == '(':
                st.append(('(', i))
                output_str += ' '
            else:
                output_str += ' '
        while len(st) > 0:
            output_str = output_str[:st[-1][1]] + 'x' + output_str[st[-1][1]+1:]
            st.pop()
        print(input_str)
        print(output_str)







