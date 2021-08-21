def solution(genres, plays):
  answer = []
  songs = dict()
  playCnt = dict()

  for i in range(len(genres)):
    songs[genres[i]] = songs.get(genres[i], []) + [(plays[i], i)]
    playCnt[genres[i]] = playCnt.get(genres[i], 0) + plays[i]
  
  playCnt = sorted(playCnt.items(), key = lambda x:x[1], reverse= True)

  for key in songs.keys():
    songs[key].sort(key = lambda x:(-x[0], x[1]))

  for played in playCnt:
    if len(songs[played[0]]) > 1:
      for i in range(2):
        cnt, idx = songs[played[0]][i]
        answer.append(idx)
        
  return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))