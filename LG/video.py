def converter(times):
    if isinstance(times, str) and len(times) == 5:
        # 문자열을 총 int로 바꿔주기
        m,s = times.split(':')
        return int(m) * 60 + int(s)
    elif isinstance(times, int):
        # 시간을 문자열로 변경하기
        m, s = times // 60 , times % 60
        print(m,s)
        m = f'0{m}' if m < 10 else f'{m}'
        s = f'0{s}' if s < 10 else f'{s}'
        return f'{m}:{s}'
        
def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    end_position = converter(video_len)
    current = converter(pos)
    op_start, op_end = converter(op_start) , converter(op_end)
    
    for cmd in commands:
        if op_start <= current <= op_end:
            current = op_end
        if cmd == 'next':
            current += 10
            if current > video_len:
                current = video_len
        elif cmd == 'prev':
            current -= 10
            if current <0:
                current = 0
    if op_start <= current <= op_end:
        current = op_end
    answer = converter(current)
    return answer
v = "34:33"
pos = "13:00"
op_start = "00:55"
op_end = "02:55"
commands = ["next", "prev"]
result = "13:00"
print(solution(v,pos,op_start,op_end,commands))