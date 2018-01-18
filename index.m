function [ n ] = index(t)
for i = 1:length(t)
    if t(i) == 1
        n = i;
    else
        n = 0
    end
end



end

