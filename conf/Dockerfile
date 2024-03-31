# FROM nginx

# RUN rm /etc/nginx/conf.d/default.conf

# ADD services.conf /etc/nginx/conf.d/

# RUN ls /etc/nginx/conf.d/


FROM nginx:latest

# Remove the default NGINX configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom NGINX configuration file
COPY services.conf /etc/nginx/conf.d/

# Expose port 80
EXPOSE 80

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]