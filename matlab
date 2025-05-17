% population_growth_simulation.m
clear; clc; close all;

%% Parameters
r = 0.1;      % intrinsic growth rate
K = 1000;     % carrying capacity
P0 = 10;      % initial population
T = 100;      % total number of time steps

%% Preallocate arrays
P_for   = zeros(1, T+1);
P_while = zeros(1, T+1);

P_for(1)   = P0;
P_while(1) = P0;

%% 1) FOR‐LOOP Simulation
for n = 1:T
    P_for(n+1) = P_for(n) + r * P_for(n) * (1 - P_for(n)/K);
end

%% 2) WHILE‐LOOP Simulation
n = 1;
while n <= T
    P_while(n+1) = P_while(n) + r * P_while(n) * (1 - P_while(n)/K);
    n = n + 1;
end

%% Visualization
figure('Position', [100 100 800 400]);

% FOR‐loop plot
subplot(1,2,1);
plot(0:T, P_for, 'LineWidth', 2);
xlabel('Time step n');
ylabel('Population P_n');
title('Logistic Growth (for‐loop)');
grid on;

% WHILE‐loop plot
subplot(1,2,2);
plot(0:T, P_while, 'LineWidth', 2);
xlabel('Time step n');
ylabel('Population P_n');
title('Logistic Growth (while‐loop)');
grid on;

% Super‐title
sgtitle('Population Growth Simulation: for vs. while');

% Save figure if desired
% saveas(gcf, 'population_growth_comparison.png');
