%% 특별 가위바위보
## 매트랩 표 구현
k = input('경우의 수 입력하시오.  ');  % 경우의 수
r = input('반복 수를 입력하시오.  ');  % 반복의 수

for n = 1:10 % 사람의 수
    Player = zeros(n+1,r);

    for i = 1:r
        player_rpc = randi([1,k],1,n);
        for j = 1:k
           if(nnz(player_rpc == j) == 1)
                Player(find(player_rpc == j),i) = 1/n;
                Player(n+1,i) = Player(n+1,i) + 1/n;
           end
        end   
    end
    Player = [Player, sum(Player,2)];
    Player(n+1, r+1) = Player(n+1, r+1)/r;
    plot(n,Player(n+1, r+1),'-o')
    hold on
    writematrix(Player,'data'+string(n)+'.dat');
end
%% 기본 공식
N = 1:10; % 사람의 수
y = ((k-1)/k).^(N-1); 
plot(N,y)
xlabel('사람의 수')
ylabel('평균 이길 확률')
hold on