FROM python:3.7-slim-stretch

ARG python_version=3.7
ARG user_name=test_user
ARG user_home=/home
ARG app_dir=${user_home}/app

COPY . / ${app_dir}/
WORKDIR ${app_dir}
ENV PYTHONPATH=.
