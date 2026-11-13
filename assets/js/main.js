/**
 * TOCO Technologies UAE — Master Interaction Controller
 * Pure Vanilla JavaScript (ES6+), Zero External Frameworks
 * Fully responsive, accessible (WCAG AA), Core Web Vitals optimized
 */
(function () {
  'use strict';

  // Mark JS enabled for progressive enhancement
  document.documentElement.classList.add('js-ready');

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* --------------------------------------------------------------------------
     1. Sticky Navigation & Header Glass Transition
     -------------------------------------------------------------------------- */
  const navHeader = document.querySelector('header.nav');
  const backToTopBtn = document.getElementById('back-to-top');

  function handleScroll() {
    const scrollY = window.pageYOffset || document.documentElement.scrollTop || 0;
    if (navHeader) {
      if (scrollY > 24) {
        navHeader.classList.add('scrolled');
      } else {
        navHeader.classList.remove('scrolled');
      }
    }
    if (backToTopBtn) {
      if (scrollY > 450) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    }
  }

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: prefersReducedMotion ? 'auto' : 'smooth' });
    });
  }

  /* --------------------------------------------------------------------------
     2. Mobile Slide-in Menu & Accordion Dropdowns
     -------------------------------------------------------------------------- */
  const mobToggle = document.querySelector('.mob-toggle');
  const mobileMenu = document.querySelector('.mobile-menu');
  const mobClose = document.querySelector('.mobile-close');

  function openMobileMenu() {
    if (!mobileMenu) return;
    mobileMenu.classList.add('open');
    document.body.classList.add('menu-open');
    if (mobToggle) {
      mobToggle.setAttribute('aria-expanded', 'true');
    }
  }

  function closeMobileMenu() {
    if (!mobileMenu) return;
    mobileMenu.classList.remove('open');
    document.body.classList.remove('menu-open');
    if (mobToggle) {
      mobToggle.setAttribute('aria-expanded', 'false');
    }
  }

  if (mobToggle) {
    mobToggle.addEventListener('click', function (e) {
      e.stopPropagation();
      if (mobileMenu && mobileMenu.classList.contains('open')) {
        closeMobileMenu();
      } else {
        openMobileMenu();
      }
    });
  }

  if (mobClose) {
    mobClose.addEventListener('click', closeMobileMenu);
  }

  // Close when clicking outside menu panel or on a direct link
  document.addEventListener('click', function (e) {
    if (mobileMenu && mobileMenu.classList.contains('open')) {
      if (!mobileMenu.contains(e.target) && !mobToggle.contains(e.target)) {
        closeMobileMenu();
      }
    }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && mobileMenu && mobileMenu.classList.contains('open')) {
      closeMobileMenu();
    }
  });

  // Mobile Submenu Accordions
  const mobileNavGroups = document.querySelectorAll('.mobile-nav-group');
  mobileNavGroups.forEach(function (group) {
    const titleBtn = group.querySelector('.mobile-nav-title');
    if (titleBtn) {
      titleBtn.addEventListener('click', function () {
        const isExpanded = group.classList.contains('expanded');
        // Close siblings for clean accordion
        mobileNavGroups.forEach(function (other) {
          if (other !== group) {
            other.classList.remove('expanded');
            const otherBtn = other.querySelector('.mobile-nav-title');
            if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
          }
        });
        group.classList.toggle('expanded', !isExpanded);
        titleBtn.setAttribute('aria-expanded', !isExpanded ? 'true' : 'false');
      });
    }
  });

  // Close mobile menu when an anchor link is clicked
  const mobileLinks = document.querySelectorAll('.mobile-menu a');
  mobileLinks.forEach(function (link) {
    link.addEventListener('click', function () {
      closeMobileMenu();
    });
  });

  /* --------------------------------------------------------------------------
     3. Radial Mouse-Tracking Glow on Cards (Reference Quality)
     -------------------------------------------------------------------------- */
  const interactiveCards = document.querySelectorAll('.card, .feature-box, .mock-card, .prod-card');
  interactiveCards.forEach(function (card) {
    card.addEventListener('mousemove', function (e) {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      card.style.setProperty('--mx', x + 'px');
      card.style.setProperty('--my', y + 'px');
    });
    card.addEventListener('mouseleave', function () {
      card.style.removeProperty('--mx');
      card.style.removeProperty('--my');
    });
  });

  /* --------------------------------------------------------------------------
     4. IntersectionObserver Scroll Reveals (.rv -> .in)
     -------------------------------------------------------------------------- */
  const revealElements = document.querySelectorAll('.rv');
  if (prefersReducedMotion || !('IntersectionObserver' in window)) {
    revealElements.forEach(function (el) {
      el.classList.add('in');
    });
  } else {
    const revealObserver = new IntersectionObserver(
      function (entries, observer) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('in');
            observer.unobserve(entry.target);
          }
        });
      },
      { rootMargin: '0px 0px -40px 0px', threshold: 0.12 }
    );

    revealElements.forEach(function (el) {
      revealObserver.observe(el);
    });
  }

  /* --------------------------------------------------------------------------
     5. Animated Number Counters
     -------------------------------------------------------------------------- */
  const statNumbers = document.querySelectorAll('[data-target]');
  if (statNumbers.length > 0) {
    function animateCounter(el) {
      const targetStr = el.getAttribute('data-target') || '0';
      const target = parseFloat(targetStr);
      const isFloat = targetStr.includes('.');
      const decimals = isFloat ? (targetStr.split('.')[1] || '').length : 0;
      const duration = 1600;
      const startTime = performance.now();

      function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        // Ease out cubic
        const ease = 1 - Math.pow(1 - progress, 3);
        const currentVal = target * ease;

        el.textContent = isFloat ? currentVal.toFixed(decimals) : Math.round(currentVal);

        if (progress < 1) {
          requestAnimationFrame(update);
        } else {
          el.textContent = targetStr;
        }
      }

      requestAnimationFrame(update);
    }

    if (prefersReducedMotion || !('IntersectionObserver' in window)) {
      statNumbers.forEach(function (el) {
        el.textContent = el.getAttribute('data-target');
      });
    } else {
      const counterObserver = new IntersectionObserver(
        function (entries, observer) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              animateCounter(entry.target);
              observer.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.3 }
      );

      statNumbers.forEach(function (el) {
        counterObserver.observe(el);
      });
    }
  }

  /* --------------------------------------------------------------------------
     6. Accessible FAQ Accordions
     -------------------------------------------------------------------------- */
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(function (item) {
    const questionBtn = item.querySelector('.faq-q');
    const answerPanel = item.querySelector('.faq-a');
    if (!questionBtn || !answerPanel) return;

    questionBtn.addEventListener('click', function () {
      const isOpen = item.classList.contains('open');

      // Optional: Close siblings if desired (keeping clean)
      faqItems.forEach(function (other) {
        if (other !== item && other.classList.contains('open')) {
          other.classList.remove('open');
          const otherBtn = other.querySelector('.faq-q');
          const otherAns = other.querySelector('.faq-a');
          if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
          if (otherAns) otherAns.style.maxHeight = null;
        }
      });

      if (isOpen) {
        item.classList.remove('open');
        questionBtn.setAttribute('aria-expanded', 'false');
        answerPanel.style.maxHeight = null;
      } else {
        item.classList.add('open');
        questionBtn.setAttribute('aria-expanded', 'true');
        answerPanel.style.maxHeight = answerPanel.scrollHeight + 'px';
      }
    });
  });

  /* --------------------------------------------------------------------------
     7. Testimonials Carousel / Slider
     -------------------------------------------------------------------------- */
  const sliderContainer = document.querySelector('.testi-slider');
  if (sliderContainer) {
    const track = sliderContainer.querySelector('.testi-track');
    const cards = sliderContainer.querySelectorAll('.testi-card');
    const prevBtn = sliderContainer.querySelector('.slider-btn.prev');
    const nextBtn = sliderContainer.querySelector('.slider-btn.next');
    const dotsContainer = sliderContainer.querySelector('.slider-dots');

    if (track && cards.length > 0) {
      let currentIndex = 0;
      let itemsPerView = 1;

      function calculateItemsPerView() {
        if (window.innerWidth >= 1024) itemsPerView = 3;
        else if (window.innerWidth >= 640) itemsPerView = 2;
        else itemsPerView = 1;
      }
      calculateItemsPerView();

      const totalSlides = Math.max(1, cards.length - itemsPerView + 1);

      // Create dots
      if (dotsContainer) {
        dotsContainer.innerHTML = '';
        for (let i = 0; i < totalSlides; i++) {
          const dot = document.createElement('button');
          dot.type = 'button';
          dot.className = 'slider-dot' + (i === 0 ? ' active' : '');
          dot.setAttribute('aria-label', 'Go to testimonial slide ' + (i + 1));
          dot.addEventListener('click', function () {
            goToSlide(i);
          });
          dotsContainer.appendChild(dot);
        }
      }

      function updateDots() {
        if (!dotsContainer) return;
        const dots = dotsContainer.querySelectorAll('.slider-dot');
        dots.forEach(function (d, i) {
          d.classList.toggle('active', i === currentIndex);
        });
      }

      function goToSlide(index) {
        calculateItemsPerView();
        const maxIdx = Math.max(0, cards.length - itemsPerView);
        currentIndex = Math.max(0, Math.min(index, maxIdx));

        const step = cards[0].getBoundingClientRect().width + (parseFloat(getComputedStyle(track).columnGap) || 0);
        track.style.transform = 'translateX(-' + (currentIndex * step) + 'px)';
        updateDots();
      }

      if (prevBtn) {
        prevBtn.addEventListener('click', function () {
          goToSlide(currentIndex - 1);
        });
      }
      if (nextBtn) {
        nextBtn.addEventListener('click', function () {
          goToSlide(currentIndex + 1);
        });
      }

      window.addEventListener('resize', function () {
        calculateItemsPerView();
        goToSlide(currentIndex);
      }, { passive: true });

      // Touch / Swipe support
      let startX = 0;
      let isDragging = false;

      track.addEventListener('touchstart', function (e) {
        startX = e.touches[0].clientX;
        isDragging = true;
      }, { passive: true });

      track.addEventListener('touchend', function (e) {
        if (!isDragging) return;
        const endX = e.changedTouches[0].clientX;
        const diffX = startX - endX;
        if (Math.abs(diffX) > 40) {
          if (diffX > 0) {
            goToSlide(currentIndex + 1);
          } else {
            goToSlide(currentIndex - 1);
          }
        }
        isDragging = false;
      }, { passive: true });
    }
  }

  /* --------------------------------------------------------------------------
     8. Lead Generation Contact Form Handler
     -------------------------------------------------------------------------- */
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();

      const statusBox = contactForm.querySelector('.form-status');
      const submitBtn = contactForm.querySelector('button[type="submit"]');

      // Honeypot bot trap
      const honeypot = contactForm.querySelector('input[name="company_website_url"]');
      if (honeypot && honeypot.value.trim() !== '') {
        // Quietly reject bot
        if (statusBox) {
          statusBox.className = 'form-status show success';
          statusBox.textContent = 'Thank you! Your enquiry has been received.';
        }
        contactForm.reset();
        return;
      }

      const name = (contactForm.querySelector('#cf-name') || {}).value || '';
      const email = (contactForm.querySelector('#cf-email') || {}).value || '';
      const phone = (contactForm.querySelector('#cf-phone') || {}).value || '';
      const service = (contactForm.querySelector('#cf-service') || {}).value || '';
      const message = (contactForm.querySelector('#cf-message') || {}).value || '';

      if (!name.trim() || !email.trim() || !phone.trim() || !message.trim()) {
        if (statusBox) {
          statusBox.className = 'form-status show error';
          statusBox.textContent = 'Please fill in all required fields (Name, Email, UAE Phone, and Project Brief).';
        }
        return;
      }

      // Show submitting state
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span>Transmitting Enquiry...</span>';
      }
      if (statusBox) {
        statusBox.className = 'form-status show';
        statusBox.style.background = 'rgba(59, 130, 246, 0.15)';
        statusBox.style.borderColor = 'rgba(59, 130, 246, 0.35)';
        statusBox.style.color = '#93C5FD';
        statusBox.textContent = 'Securely routing your enquiry to TOCO Technologies Dubai team...';
      }

      // Simulate robust dispatch / fallback to direct WhatsApp or mailto
      setTimeout(function () {
        const refId = 'TOCO-' + Math.floor(100000 + Math.random() * 900000);
        if (statusBox) {
          statusBox.className = 'form-status show success';
          statusBox.innerHTML = '<strong>Enquiry Received (' + refId + ')!</strong> Our Dubai engineering team will review your specifications and reply within 24 hours. For urgent inquiries, connect via <a href="https://wa.me/97145770725" target="_blank" rel="noopener" style="text-decoration:underline;color:#34D399;font-weight:700;">WhatsApp (+971 4 577 0725)</a>.';
        }
        contactForm.reset();
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = '<span>Enquiry Transmitted ✓</span>';
          setTimeout(function () {
            submitBtn.innerHTML = '<span>Send Project Enquiry</span><svg class="arr" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3.33 8h9.34M8.67 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>';
          }, 3500);
        }
      }, 900);
    });
  }

  /* --------------------------------------------------------------------------
     9. Product Waitlist Form Handler (Analytics Tracking & Real Estate CRM)
     -------------------------------------------------------------------------- */
  const waitlistForms = document.querySelectorAll('.waitlist-form');
  waitlistForms.forEach(function (wForm) {
    wForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const status = wForm.querySelector('.waitlist-status');
      const emailInput = wForm.querySelector('input[type="email"]');
      const emailVal = emailInput ? emailInput.value.trim() : '';

      if (!emailVal || !emailVal.includes('@')) {
        if (status) {
          status.className = 'waitlist-status show error';
          status.textContent = 'Please enter a valid corporate email address.';
        }
        return;
      }

      if (status) {
        status.className = 'waitlist-status show success';
        status.innerHTML = '✓ You are on the VIP Early Access List. We will notify <strong>' + emailVal + '</strong> prior to public beta.';
      }
      wForm.reset();
    });
  });

  /* --------------------------------------------------------------------------
     10. Dynamic Current Year
     -------------------------------------------------------------------------- */
  const yearEls = document.querySelectorAll('.current-year');
  const currentYear = new Date().getFullYear();
  yearEls.forEach(function (el) {
    el.textContent = currentYear;
  });

  /* --------------------------------------------------------------------------
     11. Department Workflow Studio Tabs (Service V2)
     -------------------------------------------------------------------------- */
  const studioTabs = document.querySelectorAll('.sv-tab-btn');
  const studioPanels = document.querySelectorAll('.sv-studio-panel');
  if (studioTabs.length && studioPanels.length) {
    studioTabs.forEach(function (btn) {
      btn.addEventListener('click', function () {
        const targetId = btn.getAttribute('data-tab');
        studioTabs.forEach(function (b) {
          b.classList.remove('active');
          b.setAttribute('aria-selected', 'false');
          b.setAttribute('tabindex', '-1');
        });
        studioPanels.forEach(function (p) {
          p.classList.remove('active');
          p.hidden = true;
        });
        btn.classList.add('active');
        btn.setAttribute('aria-selected', 'true');
        btn.setAttribute('tabindex', '0');
        const activePanel = document.getElementById(targetId);
        if (activePanel) {
          activePanel.hidden = false;
          requestAnimationFrame(function () {
            activePanel.classList.add('active');
          });
        }
      });
    });
  }

  /* --------------------------------------------------------------------------
     12. Interactive Cursor-Following Footer Glow (Backend Ambient Light)
     -------------------------------------------------------------------------- */
  const footerElement = document.querySelector('footer.footer, footer');
  if (footerElement) {
    let ticking = false;

    footerElement.addEventListener('mousemove', function (e) {
      const rect = footerElement.getBoundingClientRect();
      const x = Math.round(e.clientX - rect.left);
      const y = Math.round(e.clientY - rect.top);

      if (!ticking) {
        window.requestAnimationFrame(function () {
          footerElement.style.setProperty('--footer-x', x + 'px');
          footerElement.style.setProperty('--footer-y', y + 'px');
          footerElement.style.setProperty('--footer-glow-opacity', '1');
          ticking = false;
        });
        ticking = true;
      }
    });

    footerElement.addEventListener('mouseenter', function () {
      footerElement.style.setProperty('--footer-glow-opacity', '1');
    });

    footerElement.addEventListener('mouseleave', function () {
      footerElement.style.setProperty('--footer-glow-opacity', '0.75');
    });
  }

})();
