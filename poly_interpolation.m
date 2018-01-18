x = [0:6]
y = [0 1 4 9 16 25 36];
n= length(x);

sum = 0;

for j = 1:n
    v=1;
    for k = 1:n
        if j~=k
            v = conv(v, (poly(x(k))))/(x(j) - x(k));
        end
    end
    
    sum = sum + v.*y(j);
end
index(sum)